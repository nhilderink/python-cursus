visitors = {
    "109.184.11.34": {
        "ua": "Mozilla/5.0 (Windows NT 6.0; rv:34.0)",
        "count": 4
    },
    "87.159.214.230": {
        "ua": "T-Online Browser (Windows NT 6.1; de)",
        "count": 1
    }
}

# ua1 = visitors["109.184.11.34"]["ua"]
# ua2 = visitors["87.159.214.230"]["ua"]
# print(ua1)
# print(ua2)

total_count = 0
for key in visitors:
    ua = visitors[key]["ua"]
    ct = visitors[key]["count"]
    total_count = total_count + ct
    print(ua)

print(total_count)
