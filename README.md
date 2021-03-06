# jekyll-theme-minimax

Minimax is a Jekyll theme based on [Minima](https://github.com/jekyll/minima) with a little extension.

- [jekyll-theme-minimax](#jekyll-theme-minimax)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Tag Cloud](#tag-cloud)
    - [Category Archive](#category-archive)
    - [Mathjax](#mathjax)
    - [Table of Contents](#table-of-contents)
  - [Contributing](#contributing)
  - [Development](#development)
  - [License](#license)

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "jekyll-theme-minimax"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: jekyll-theme-minimax
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-theme-minimax

## Usage

### Tag Cloud

In anywhere you want to show the tag cloud, insert `{% include tag_cloud.html %}`. 

You can manually write a page for each tag to list all posts that are labeled with the tag. For example, you want to show all posts labeled with `jekyll`, then create a page `tag/jekyll.md`:

```
---
layout: tag_page
tag: jekyll
---
```

*Want free your hands*? Run a [script](scripts/tag-generator.py) to generate all tag pages automatically: `python scripts/tag-generator.py`.

### Category Archive

`{% include category_archive.html %}`

### Mathjax

Minimax support Mathjax. You can write mathematical formulas in your posts if you set the `math` front matter to be `true` in these posts. [Example](_posts/2019-02-21-test-mathjax.md).

### Table of Contents

You can insert `{% include toc.html %}` at anywhere you want to automatically generate a table of contents. Don't forget specify the below lines in `_config.yml`.

```
markdown: kramdown
kramdown:
  parse_block_html: true
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/hello. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`.

Your theme is setup just like a normal Jekyll site! To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000`. This starts a Jekyll server using your theme. Add pages, documents, data, etc. like normal to test your theme's contents. As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

When your theme is released, only the files in `_layouts`, `_includes`, `_sass` and `assets` tracked with Git will be bundled.
To add a custom directory to your theme-gem, please edit the regexp in `jekyll-theme-minimax.gemspec` accordingly.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

