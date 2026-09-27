import urllib.request
import json

url = "https://api.github.com/repos/ramSeraph/indian_land_features/releases"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        releases = json.loads(resp.read().decode("utf-8"))
    
    ngdr_assets = []
    for r in releases:
        tag = r.get("tag_name")
        for asset in r.get("assets", []):
            name = asset.get("name", "")
            if any(k in name.lower() for k in ["ngdr", "geology", "lithology"]):
                ngdr_assets.append({
                    "tag": tag,
                    "name": name,
                    "size_mb": round(asset.get("size", 0) / (1024 * 1024), 2),
                    "url": asset.get("browser_download_url")
                })
                
    print(f"Found {len(ngdr_assets)} NGDR / Geology / Lithology assets:")
    for a in ngdr_assets:
        print(f" - [{a['name']}] ({a['size_mb']} MB): {a['url']}")
        
    with open("data/ngdr_releases.json", "w", encoding="utf-8") as f:
        json.dump(ngdr_assets, f, indent=2)
except Exception as e:
    print(f"Error: {e}")
