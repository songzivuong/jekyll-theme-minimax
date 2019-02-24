# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "jekyll-theme-minimax"
  spec.version       = "0.7.0"
  spec.authors       = ["Songzi Vuong"]
  spec.email         = ["songzivuong@gmail.com"]

  spec.summary       = "Minimax is a Jekyll theme based on Minima with a little extension."
  spec.homepage      = "https://github.com/songzivuong/jekyll-theme-minimax"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 3.8"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.9"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.1"
  spec.add_development_dependency "bundler", "~> 1.16"
  spec.add_development_dependency "rake", "~> 12.0"
end
