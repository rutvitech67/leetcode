class Solution(object):
    def numUniqueEmails(self, emails):
        return len({
            (email.split('@')[0].split('+')[0].replace('.', ''), email.split('@')[1])
            for email in emails
        })

