# This installs flask
#Author: Mostapha BOUDAD

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
