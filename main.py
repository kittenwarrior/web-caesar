import webapp2
import caesar


def build_page(textarea_content):
            rot_label = "<label>Rotate by:</label>"
            rotation_input = "<input type='number' name='rotation'/>"

            message_label = "<label>Type a message:</label>"
            textarea = "<textarea name='message'>" + textarea_content + "</textarea>"

            submit = "<input type='submit'/>"
            form = ("<form method='post'>" +
                    rot_label + rotation_input + "<br>" +
                    message_label + textarea + "<br>" +
                    submit + "</form>")

            header = "<h2>Web Caesar</h2>"

            return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        content = build_page(encrypted_message)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
