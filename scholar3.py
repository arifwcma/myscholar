from scholarly import scholarly

author = scholarly.search_author_id("dfBU3voAAAAJ")
author = scholarly.fill(author, sections=["publications"])

with open("titles2.txt", "w", encoding="utf-8") as f:
    for pub in author["publications"]:
        pub_filled = scholarly.fill(pub)
        title = pub_filled.get("bib", {}).get("title", "")
        f.write(title + "\n\n")
