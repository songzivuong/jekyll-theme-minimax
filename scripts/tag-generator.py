import glob
import os

post_dir = '_posts/'
draft_dir = '_drafts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')
filenames.extend(glob.glob(draft_dir + '*md'))

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag_page\ntag: ' + tag + '\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())