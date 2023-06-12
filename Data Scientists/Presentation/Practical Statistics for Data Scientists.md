---
marp: true

theme: dracula
# class: invert
# layout: cover
# math: latex 
paginate: true
# inlineSVG: true
# backgroundColor: #fff
# backgroundImage: url('https://marp.app/assets/hero-background.svg')
author: Rene Verinaud Anguita Junior
title: Planejamento da expansão de sistemas de distribuição com tomadas de decisão multicritério utilizando a metaheurística Busca Tabu
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

---
<!--  _class: invert -->
<!-- _color: white -->
<!-- _paginate: skip -->

# Practical Statistics for Data Scientists

---
<!--  _class: invert -->
<!-- _color: white -->

# Type of Mean
---

# Mean
<div class="columns">
<div>

- Mean or average value;

- Sum of all the values divided by the number of values.
</div>
<div>

$$
\overline X = \frac{\sum_{i}^{n} x_i}{n}
$$
</div>
</div>

---

# Trimmed mean
<div class="columns">
<div>

- Variation of the mean or trimmed mean;

- Dropping a fixed number (p) of values at each end;

- **Eliminates the influence of extreme value.**

</div>
<div>

$$
\overline X = \frac{\sum_{i = p + 1}^{n - p} x_i}{n - 2p}
$$
</div>
</div>

---

# Weighted mean

There are two main motivations for using a weighted mean:
- **Some values are intrinsically more variable than others, and highly variable observations are given a lower weight;**
- **The data collected does not equally represent the different groups that we are interested in measuring.**



$$
\overline X_w = \frac{\sum_{i = 1}^{n} w_i x_i}{\sum_{i}^{n} w_i}
$$

---
