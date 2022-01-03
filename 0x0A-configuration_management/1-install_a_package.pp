#A puppet file that installs puppet-lint

package {'puppet-lint':
    ensure => '2.5.0',
    provider => 'gem',
}
