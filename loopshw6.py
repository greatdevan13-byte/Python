blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
Total_views=0
Trending_count=0

for x in blog_views:
    Total_views+=x

    if x>1000:
        print("Trending")
        Trending_count+=1
    elif x<1000 and Total_views>500:
        print("Average")
    else:
        print("Low traffic")

print("Total views :",Total_views)
print("Trending counts :",Trending_count)        
        
