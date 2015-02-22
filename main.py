#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form = '''
<form method = 'post'>
	<label>username
		<input type = 'text' name = 'username'>
	</label><br>
	</lable>password
		<input type = 'password' name='password'>
	</label><br>
	<label>verify
		<input type = 'password' name='verify'>
	</label><br>
	<label>email
		<input type='text' name='email'>
	</label><br>
		<input type='submit' name='submit'>
</form>'''
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#self.response.headers['Content-Type'] = 'text/HTML'
        self.response.out.write(form)

    def post(self):
    	#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)
		user_input = self.request.get('username')
		'''user_output =''
		accumulator = ''
		for i in user_input:
			i = chr((((ord(i) - 97) + 13) % 26) + 97)
			accumulator += i
		user_output = accumulator'''
		self.response.out.write(user_input)

class ROTC(webapp2.RequestHandler): 
	def get(self):
		'''q = self.request.get('q')
		self.response.out.write(q)'''
		self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)
		user_input = self.request.get('user_input')
		user_output =''
		accumulator = ''
		for i in user_input:
			i = chr((((ord(i) - 97) + 13) % 26) + 97)
			accumulator += i
		user_output = accumulator

app = webapp2.WSGIApplication([('/', MainHandler), ('/rotc', ROTC)], 
							debug=True)
