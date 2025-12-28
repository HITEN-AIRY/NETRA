# netra/active/wordlist.py

from netra.intelligence.wordlist_expander import AIWordlistExpander


DEFAULT_WORDLIST = [
    "www", "api", "admin", "auth", "dev",
    "test", "stage", "staging", "portal",
    "internal", "dashboard", "beta"
]


class WordlistProvider:
    def __init__(self, ai_enabled: bool = False):
        self.words = set(DEFAULT_WORDLIST)
        self.ai_enabled = ai_enabled
        self.expander = AIWordlistExpander()

    def expand_with_ai(self, discovered_domains):
        ai_words = self.expander.expand(discovered_domains)
        self.words.update(ai_words)

    def generate(self, root_domain: str):
        return [f"{word}.{root_domain}" for word in self.words]
