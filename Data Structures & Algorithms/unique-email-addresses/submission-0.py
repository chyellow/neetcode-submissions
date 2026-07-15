class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local = ""
            first, second = email.split("@")
            first = first.split("+")[0]
            first = first.replace(".", "")
            local = first + second
            unique.add(local)
        
        return len(unique)
