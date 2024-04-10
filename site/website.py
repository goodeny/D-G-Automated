class Website:
    def __init__(self):
        self.archive = 'Pedido-de-namoro-main/timeline.html'

    def insert(self, img, title, description):
        #print(img)
        new_line = f'<div class="timeline-item"><div class="timeline__content"><img class="timeline__img" src="./img/{img}"/><h2 class="timeline__content-title">{title}</h2><p class="timeline__content-desc">{description}</p></div></div>\n      <!--python-->\n'
        n = 0
        with open(self.archive, 'r+', encoding='utf-8') as arch:
            conteudo_html = arch.readlines()
        for num, i in enumerate(conteudo_html):
            if "<!-- D&G-AUTOMATED -->" in i:
                if num >= n:
                    n = num
        with open(self.archive, 'r+', encoding='utf-8') as arch:
            conteudo_html = arch.readlines()
            conteudo_html.insert(n, new_line)
            arch.seek(0)
            arch.writelines(conteudo_html)