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

rotc_input = '''
<form action='/rotc' method='post'>
	<fieldset>
		<legend>input</legend>
		<label>encryption word
		<input type = 'text' name = 'word'>
		</label><br>
		<label>no. of shifts
		<input type = 'text' name='shifts'>
		</label><br>
		<input type='submit' name='submit'>
	</fieldset>
</form>'''

loginpage_form = '''
<form action='/loginpage' method='get'>
	<fieldset>
		<legend>login information</legend>
		<label for='username'>Username</label>
		<input type='text' id='username' name='username'><br>
		<label for='password'>Password</label>
		<input type='password' id='password' name='password'><br>
		<label for='verifypassword'>Verify Password</label>
		<input type='password' id='verifypassword' name='verifypassword'><br>
		Gender:
		<label for='male'>Male</label>
		<input type='radio' name='gender' value='male' id='male'><br>
		<label for='female'>Female</label>
		<input type='radio' name='gender' value='female' id='female'><br>
		Email:
		<input type='text' name='email'>
	</fieldset>
<form>
'''
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#self.response.headers['Content-Type'] = 'text/HTML'
    	self.response.out.write(rotc_input)

    def post(self):
		#self.response.out.write(self.request)
		pass

class ROTC(webapp2.RequestHandler): 
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		word = self.request.get('word')
		shift = self.request.get('shifts')
		if (word == 'samman') and (shift == 'samman'):
			self.redirect('/loginpage')
		else:
			output = rotmaker(word, shift)
			self.response.out.write(output)

class LoginPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(loginpage_form)
		uname = self.request.get('username')
		password = self.request.get('password')
		verifypassword = self.request.get('verifypassword')
		




app = webapp2.WSGIApplication([('/', MainHandler), ('/rotc', ROTC), ('/loginpage', LoginPage)], 
							debug=True)


def rotmaker(word, shift):
	accumul = ''
	shift = int(shift)
	for i in word:
		i = chr(((ord(i) - 97 + shift) % 26) + 97)
		accumul += i
	return accumul

