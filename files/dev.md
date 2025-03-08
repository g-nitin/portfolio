# Development Commands and Fixes

## Commands
Some helpful commands for when developing:

```shell
bundle install
bundle update
bundle add webrick
bundle exec jekyll serve --baseurl=""
```

# Fixes

### Issue: March 8th, 2025
- Issue at `bundle install`. Error: `Because nokogiri = 1.16.2 depends on Ruby >= 3.0.0   and nokogiri >= 1.16.2, < 1.16.3 depends on Ruby >= 3.0.0, < 3.4.dev,   nokogiri >= 1.16.2, < 1.16.3 requires Ruby >= 3.0.0`
- Had to update Gem version to 3.3.4 with `ruby-install 3.3.4` and ensure with `chruby 3.3.4`
- Had to add to `~/.zshrc` with:
    ```bash
    echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
    echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
    echo "chruby ruby-3.3.4" >> ~/.zshrc
    ```
- Exit shell
- Add `.ruby-version` file
- Update `Gemfile` to dynamically load ruby version
- Checked system version has been updated with `ruby -v`
- `gem install bundler`
- `bundle install`
- Sources used:
  - [How and Why to Upgrade the Ruby Version in Your Project](https://www.rubyonmac.dev/how-to-upgrade-the-ruby-version-in-your-project)
  - [The fastest and easiest way to install Ruby on a Mac in 2025](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/)