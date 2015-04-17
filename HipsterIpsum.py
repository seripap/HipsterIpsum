import sublime
import sublime_plugin
import random
import re

class HipsterIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=10):

        selections = self.view.sel()
        for selection in selections:

            # Nothing here
            para = ""

            # words from the original Lorum ipsum text
            words = "+1 3 8-bit 90's Actually Aesthetic American Anderson Apparel Art Artisan Asymmetrical Austin Authentic Banh Banjo Banksy Beard Before Bespoke Bicycle Biodiesel Bitters Blog Blue Bottle Brooklyn Brunch Bushwick Butcher Cardigan Carles Chambray Chia Chillwave Church-key Cliche Cornhole Cosby Craft Cray Cred DIY Deep Direct Disrupt Distillery Dreamcatcher Drinking Echo Ennui Ethical Ethnic Etsy Fanny Fap Farm-to-table Fashion Fingerstache Fixie Flannel Flexitarian Food Forage Four Freegan Future Gastropub Gentrify Gluten-free Godard Hashtag Hella Helvetica High Hoodie IPhone Intelligentsia Irony Jean Kale Keffiyeh Keytar Kitsch Kogi Leggings Letterpress Life Literally Lo-fi Locavore Lomo Marfa Master McSweeney's Meggings Meh Messenger Mixtape Mlkshk Mumblecore Mustache Narwhal Neutra Next Occupy Odd Organic PBR PBR&B Paleo Park Photo Pickled Pinterest Pitchfork Plaid Polaroid Pop-up Pork Portland Post-ironic Pour-over Pug Put Quinoa Raw Readymade Retro Richardson Roof Salvia Sartorial Scenester Schlitz Seitan Selfies Selvage Semiotics Shabby Shoreditch Single-origin Skateboard Slow-carb Small Squid Sriracha Street Stumptown Sustainable Swag Synth Tattooed Terry Thundercats Tofu Tonx Tote Tousled Truffaut Trust Try-hard Tumblr Twee Typewriter Ugh Umami VHS Vegan Vice Vinyl Viral Wayfarers Wes Whatever Williamsburg Wolf XOXO YOLO You Yr a actually aesthetic art artisan asymmetrical authentic axe bag banh banjo batch beard beer before belly bespoke bicycle biodiesel bird bitters blog booth brunch butcher cardigan chambray chia chic chillwave chips church-key cleanse cliche coffee cornhole craft cray cred deep denim direct disrupt distillery dreamcatcher drinking ennui ethical ethnic fanny fap farm-to-table fashion fingerstache fixie flannel flexitarian food forage four freegan fund gastropub gentrify gluten-free hashtag haven't heard hella hoodie iPhone irony it jean kale keffiyeh keytar kitsch kogi leggings letterpress level literally lo-fi locavore loko lomo master meggings meh messenger mi mixtape mlkshk moon mumblecore mustache narwhal next occupy of on organic out pack paleo party photo pickled plaid polaroid pop-up pork post-ironic pour-over probably pug put quinoa raw readymade retro rights roof salvia sartorial scenester seitan selfies selvage semiotics shabby shorts single-origin skateboard slow-carb small sold squid sriracha street stumptown sustainable swag sweater synth tattooed them they tofu tote tousled trade truck trust try-hard twee typewriter ugh umami v vegan vinegar vinyl viral wayfarers whatever wolf you yr".split()

            # get preceding numbers (possibly with decimal separation) if available
            lastchars = self.view.substr(sublime.Region(selection.begin()-20, selection.end()))
            last = re.search("(|(\d+)(\.\d+)?)$", lastchars).group(0)

            m = str(last).split(".")

            if re.search("\d", last) and (
                (len(m) > 1 and (int(m[0]) * int(m[1])) < 1000)
                or (len(m) == 1 and int(m[0]) < 1000)
            ):
                selection = sublime.Region(selection.begin() - len(str(last)), selection.end())
            else:
                # if they wasked for too much lorem, just give 'em one - for their own safety!
                last = 1
            # could give error instead - but who wants to think that much about lorem?
            # else:
            #     print("[ERROR] too much lorem ipsum - try a smaller number")

            m = str(last).split(".")
            paras = int(m[0])

            if len(m) > 1:
                qty = int(m[1])

            for i in list(range(0, paras)):
                from random import choice
                para += choice(words).capitalize() + " "
                for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                    para += choice(words) + " "
                para += choice(words) + "."
                if i != paras and paras > 1:
                    para += "\n\n"

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

            self.view.end_edit(edit)

