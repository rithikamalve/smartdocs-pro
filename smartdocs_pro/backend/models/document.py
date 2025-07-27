from datetime import datetime

class Document:
    def __init__(self, doc_id, ext, filename, upload_time=None, metadata=None):
        self.doc_id = doc_id
        self.ext = ext
        self.filename = filename
        self.upload_time = upload_time or datetime.utcnow().isoformat()
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'ext': self.ext,
            'filename': self.filename,
            'upload_time': self.upload_time,
            'metadata': self.metadata
        } 