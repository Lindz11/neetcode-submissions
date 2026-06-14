class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hSet = set()
        for email in emails:
            local, domain = email.split("@", 1)
            valid = local.split("+", 1)
            valid = valid[0].replace('.', '')
            address = valid + domain
            hSet.add(address)
        
        return len(hSet)