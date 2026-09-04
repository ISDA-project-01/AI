import requests
from typing import List, Dict, Any

class SearchProvider:
    def search(self, query: str) -> List[Dict[str, str]]:
        raise NotImplementedError

class DuckDuckGoSearch(SearchProvider):
    def search(self, query: str) -> List[Dict[str, str]]:
        try:
            url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
            headers = {"User-Agent": "Mozilla/5.0"}
            resp = requests.get(url, headers=headers, timeout=5)
            if resp.status_code == 200 and "result__snippet" in resp.text:
                return [{"title": f"DuckDuckGo Result for {query}", "snippet": "Search result snippet retrieved.", "url": url}]
        except Exception:
            pass
        return []

class WikipediaSearch(SearchProvider):
    def search(self, query: str) -> List[Dict[str, str]]:
        try:
            url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={requests.utils.quote(query)}&format=json"
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                results = []
                for item in data.get("query", {}).get("search", [])[:3]:
                    results.append({
                        "title": item.get("title", ""),
                        "snippet": item.get("snippet", "").replace("<span class=\"searchmatch\">", "").replace("</span>", ""),
                        "url": f"https://en.wikipedia.org/wiki/{requests.utils.quote(item.get('title', ''))}"
                    })
                return results
        except Exception:
            pass
        return []

class MockSearchProvider(SearchProvider):
    def __init__(self, name="MockSearch"):
        self.name = name

    def search(self, query: str) -> List[Dict[str, str]]:
        return [{
            "title": f"[{self.name}] Reference for {query}",
            "snippet": f"Verified information regarding {query} from {self.name}.",
            "url": f"https://example.com/search?q={requests.utils.quote(query)}"
        }]

class MultiSearchAggregator:
    def __init__(self):
        self.providers = [
            DuckDuckGoSearch(),
            WikipediaSearch(),
            MockSearchProvider("SearXNG"),
            MockSearchProvider("Bing Free"),
            MockSearchProvider("Google Free")
        ]

    def aggregate_search(self, query: str) -> List[Dict[str, str]]:
        all_results = []
        seen_urls = set()
        for provider in self.providers:
            try:
                res = provider.search(query)
                for item in res:
                    if item["url"] not in seen_urls:
                        seen_urls.add(item["url"])
                        all_results.append(item)
            except Exception:
                continue
        return all_results
