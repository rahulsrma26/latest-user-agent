import os
import queue
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd


@dataclass(order=True)
class UserAgent:
    last_used: datetime
    user_agent: str = field(compare=False)


class UserAgentManager:
    Chrome = "Chrome"
    Safari = "Safari"
    Firefox = "Firefox"
    Edge = "Edge"
    Opera = "Opera"

    def __init__(
        self,
        first: int = 5,
        last: int = 3,
        cache: Optional[str] = None,
        commit_id: str = "master",
    ) -> None:
        """
        Read top user agents from a weekly updated list (from useragentstring.com)
        and returns random agement based on user's preference.

        Parameters:
            first (int): oldest allowd first visit date in terms of years from now
            last (int): oldest allowd last visit date in terms of years from now
        """
        df = None
        if cache and os.path.isfile(cache):
            m_time = os.path.getmtime(cache)
            if (datetime.now() - datetime.fromtimestamp(m_time)) < timedelta(days=7):
                df = pd.read_csv(cache)
                print("UA loaded from", cache)
        if df is None:
            df = pd.read_csv(
                f"https://raw.githubusercontent.com/rahulsrma26/user-agents/{commit_id}/data/top_user_agents.csv"
            )
            if cache:
                os.makedirs(os.path.dirname(cache), exist_ok=True)
                df.to_csv(cache, index=False)
                print("UA saved to", cache)

        df["first"] = pd.to_datetime(df["first"])
        df["last"] = pd.to_datetime(df["last"])
        first = datetime.now() - timedelta(days=365 * first)
        last = datetime.now() - timedelta(days=365 * last)
        self.df = df[(df["first"] > first) & (df["last"] > last)]
        self.q = queue.PriorityQueue()

    def random(self, browser: Optional[str] = None) -> str:
        """
        Returns random user-agent string

        Parameters:
            browser (str): Name of the browser (returns any if None)
        """
        df = self.df
        if browser:
            df = df[df["browser"] == browser]
        return df.sample().iloc[0]["ua"]

    def pooled(self, browser: Optional[str] = None, gap: int = 60 * 6) -> str:
        if not self.q.empty():
            ua = self.q.get()
            if (datetime.now() - ua.last_used) > timedelta(seconds=gap):
                ua.last_used = datetime.now()
                self.q.put(ua)
                return ua
            self.q.put(ua)
        ua = UserAgent(datetime.now(), self.random(browser))
        self.q.put(ua)
        return ua

    def remove(self, ua: UserAgent):
        q = queue.PriorityQueue()
        while not self.q.empty():
            item = self.q.get()
            if item.user_agent != ua.user_agent:
                q.put(item)
        self.q = q
