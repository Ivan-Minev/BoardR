class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    # status_seq = {
    #     'OPEN' : 'Open',
    #     'TODO' : 'Todo',
    #     'IN_PROGRESS' : 'In progress',
    #     'DONE' : 'Done',
    #     'VERIFIED' : 'Verified'}
    
    status_seq_list = ['Open', 'Todo', 'In progress', 'Done', 'Verified']

    @classmethod
    def next(cls, current):

        if current == 'Verified':
            return 'Verified'
        else:
            cur_idx = cls.status_seq_list.index(current)
            next_status_idx = cur_idx + 1
            next_status = cls.status_seq_list[next_status_idx]
            return next_status
    
    @classmethod
    def previous(cls, current):

        if current == 'Open':
            return 'Open'
        else:
            cur_idx = cls.status_seq_list.index(current)
            prev_status_idx = cur_idx - 1
            prev_status = cls.status_seq_list[prev_status_idx]
            return prev_status
        
