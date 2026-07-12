class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        mail_to_name = {}
        
        def find(mail):
            if parent[mail] != mail:
                # FIX 1: Changed square brackets [] to parentheses () for function call
                parent[mail] = find(parent[mail]) 
            return parent[mail]
        
        def union(mail1, mail2):
            # FIX 2: Call find() instead of accessing parent directly to get absolute roots
            root1, root2 = find(mail1), find(mail2)
            if root1 != root2:
                parent[root2] = root1

        for i, name_mail in enumerate(accounts):
            name = name_mail[0]
            # FIX 3: Get the first email of the CURRENT account (name_mail), not accounts[1]
            first_email = name_mail[1]

            for email in name_mail[1:]:  # Cleaner use of loop variable
                if email not in parent:
                    parent[email] = email

                mail_to_name[email] = name
                union(first_email, email)

        merged_groups = defaultdict(list)
        for email in parent:
            root = find(email)
            # FIX 4: Group emails by their root key, not roots by their email key
            merged_groups[root].append(email)
        res = []

        for root, mails in merged_groups.items():
            name = mail_to_name[root]
            res.append([name]+sorted(mails))

        return res