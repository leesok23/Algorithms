class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = {}
        for email in emails:
            domain_name = email[email.index('@'):]
            if '+' in email:
                local = email[:email.index('+')]
            else:
                local = email[:email.index('@')]
            local_name = local.replace('.', '')
            modified_email = local_name + domain_name
            if modified_email not in hashmap:
                hashmap[modified_email] = 1
        return len(hashmap)
