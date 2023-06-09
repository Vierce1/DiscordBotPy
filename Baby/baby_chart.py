import helpers
import pylab
import matplotlib.pyplot as pyplot
from matplotlib_venn import venn2, venn3, venn3_circles
import discord
import discord.ext
import helpers


def get_baby_venn():
    pyplot.figure()
    subsets = (1, 1, 1)
    # ashley_names = set(['Evelyn', 'Heidi', 'Paytona500', 'Sophia'])
    # andrew_names = set(['Evelyn', 'Heidi', 'Rosemary', 'Anya'])
    ashley_names = set(helpers.get_used_babies('Ashley', True, 8, False))
    andrew_names = set(helpers.get_used_babies('Andrew', True, 8, False))
    venn = venn2(subsets=(ashley_names, andrew_names), set_labels=('Andrew', 'Ashley', 'Shared'))

    shared_names = set(andrew_names) & set(ashley_names)
    andrew_solo_names = set(ashley_names - andrew_names)
    ashley_solo_names = set(andrew_names - ashley_names)
    shared_names_str = '\n'.join(shared_names)
    andrew_names_str = '\n '.join(andrew_solo_names)
    ashley_names_str = '\n '.join(ashley_solo_names)
    # could count up the names in each group, and if over x add a '\n' character

    venn.get_label_by_id('100').set_text(ashley_names_str)
    venn.get_label_by_id('110').set_text(shared_names_str)
    venn.get_label_by_id('010').set_text(andrew_names_str)


    pyplot.title("Baby Names")
    chart_file = "names_diagram.png"
    pyplot.savefig(chart_file) # could pass in dpi to savefig as chart's dpi to increase resolution
    chart_image = discord.File(chart_file)
    return chart_image