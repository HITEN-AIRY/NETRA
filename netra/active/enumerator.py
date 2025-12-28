# netra/active/enumerator.py

from netra.active.wordlist import WordlistProvider


class ActiveEnumerator:
    def __init__(self, root_domain: str, ai_enabled=False, known_domains=None):
        self.root_domain = root_domain
        self.wordlist = WordlistProvider(ai_enabled=ai_enabled)

        if ai_enabled and known_domains:
            self.wordlist.expand_with_ai(known_domains)

    def generate_candidates(self):
        return self.wordlist.generate(self.root_domain)
