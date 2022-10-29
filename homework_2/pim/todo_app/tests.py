from django.test import TestCase

def test_sendpost(self):
    clear_args()
    add_testfiles()
    for message in self.mbox:
        self.assertEqual(message['subject'], 'post')
        self.assertEqual(message.get_payload(), HTML_TXT)
    if not self.mbox:
        self.fail("No messages were sent")
