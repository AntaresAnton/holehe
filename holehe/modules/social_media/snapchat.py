from holehe.core import *
from holehe.localuseragent import *

async def snapchat(email, client, out):
    name = "snapchat"
    domain = "snapchat.com"
    method = "login"
    frequent_rate_limit = False

    headers = {
        "Host": "accounts.snapchat.com",
        "User-Agent": random.choice(ua["browsers"]["firefox"]),
        "Accept": "*/*",
        "Accept-Encoding": "gzip, late",
        "Content-Type": "application/json",
        "Connection": "close",
    }

    try:
        req = await client.get("https://accounts.snapchat.com", headers=headers, follow_redirects=True)
        xsrf = req.text.split('data-xsrf="')[1].split('"')[0]
        webClientId = req.text.split('ata-web-client-id="')[1].split('"')[0]
        
        headers["X-XSRF-TOKEN"] = xsrf
        headers["Cookie"] = f"xsrf_token={xsrf}; web_client_id={webClientId}"
        
        data = '{"email":' + email + ',"app":"BITMOJI_APP"}'

        response = await client.post(
            'https://accounts.snapchat.com/accounts/merlin/login', 
            headers=headers,
            data=data,
            follow_redirects=True
        )

        if response.status_code != 204:
            data = response.json()
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "exists": data["hasSnapchat"],
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
        else:
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "exists": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })

    except Exception as e:
        out.append({
            "name": name,
            "domain": domain,
            "method": method,
            "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": True,
            "exists": False,
            "emailrecovery": None,
            "phoneNumber": None,
            "others": None
        })
