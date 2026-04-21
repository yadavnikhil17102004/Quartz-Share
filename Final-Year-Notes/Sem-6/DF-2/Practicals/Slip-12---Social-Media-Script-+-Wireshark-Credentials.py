import requests

def get_github_profile(username):
    print(f"[*] Fetching profile data for GitHub user: {username}")
    url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "DF2-Practical-Script"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("\n[+] Profile Data Extracted Successfully!")
            print("-" * 40)
            print(f"Username      : {data.get('login')}")
            print(f"Name          : {data.get('name')}")
            print(f"Bio           : {data.get('bio')}")
            print(f"Followers     : {data.get('followers')}")
            print(f"Account Created: {data.get('created_at')}")
            print(f"Public Repos  : {data.get('public_repos')}")
            print("-" * 40)
        else:
            print(f"[-] API Error: {response.status_code}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    target_user = "yadavnikhil17102004" 
    get_github_profile(target_user)
