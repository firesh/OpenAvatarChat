import os
import unittest
import tempfile
from datetime import datetime
from handlers.llm.openai_compatible.chat_history_manager import ChatHistory, HistoryMessage


class TestChatHistoryLogging(unittest.TestCase):
    def test_logging_to_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            history = ChatHistory(session_id="test", log_dir=tmpdir)
            history.add_message(HistoryMessage(role="human", content="hello"))
            history.add_message(HistoryMessage(role="avatar", content="hi"))

            prefix = datetime.now().strftime("%Y%m%d-")
            log_path = os.path.join(tmpdir, f"{prefix}test.txt")
            with open(log_path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()

            self.assertEqual(lines, ["human: hello", "avatar: hi"])


if __name__ == '__main__':
    unittest.main()
