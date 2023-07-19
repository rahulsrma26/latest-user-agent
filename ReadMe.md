latest_user_agent
=================

A small package that generate user-agents that are fetched from [useragentstring.com](https://www.useragentstring.com) and are in use.

Usage
-----

```py
uam = UserAgentManager()
while (cmd := input()) != "q":
    ua = uam.pooled(gap=3)
    print(uam.q.qsize(), ua)
```

Installation
------------

```sh
pip install git+https://github.com/rahulsrma26/latest-user-agent
```

Requirements
-------------

python >= 3.8
