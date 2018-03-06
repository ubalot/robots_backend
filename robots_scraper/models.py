from django.db import models

from robots_scraper.controller import get_robots_txt, robots_extrapolation


class WebSite(models.Model):
    domain = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    robots_url = models.CharField(max_length=50)

    websites = models.Manager()

    def __str__(self):
        return self.url

    def parse_robots_txt(self):
        robots_txt = get_robots_txt(self.robots_url)
        content = robots_extrapolation(robots_txt)
        return content

    def after_save(self):
        parsed = self.parse_robots_txt()
        for user_agent, rules in parsed.items():
            _user_agent = UserAgent(website=self, user_agent=user_agent)
            _user_agent.save()
            for rule, routes in rules.items():
                _rule = Rule(user_agent=_user_agent, rule=rule)
                _rule.save()
                for route in routes:
                    _route = Route(rule=_rule, route=route)
                    _route.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.after_save()


class UserAgent(models.Model):
    website = models.ForeignKey(WebSite, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=30)

    def __str__(self):
        return self.user_agent


class Rule(models.Model):
    user_agent = models.ForeignKey(UserAgent, on_delete=models.CASCADE)
    rule = models.CharField(max_length=30)

    def __str__(self):
        return self.rule

class Route(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    route = models.CharField(max_length=50)

    def __str__(self):
        return self.route
