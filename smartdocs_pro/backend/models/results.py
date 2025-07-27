from datetime import datetime

class Results:
    def __init__(self, doc_id, ext, task, result_type, result, created_at=None):
        self.doc_id = doc_id
        self.ext = ext
        self.task = task
        self.result_type = result_type
        self.result = result
        self.created_at = created_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'ext': self.ext,
            'task': self.task,
            'result_type': self.result_type,
            'result': self.result,
            'created_at': self.created_at
        } 