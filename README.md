# Solucions
```
     <section>
        <img src="static/img/Diverse-people.jpg">
        <img src="static/img/guia-completa-entender-como-funcionan-fotos-stock.jpg">
        <img src="static/img/Man-Stock-Photos.jpg">
    </section>

section {
    display:flex;
    width:600px;
    height:430px;
}

section img {
    width:0px;
    flex-grow:1;
    object-fit: cover;
    opacity: .8;
    transition: .5s ease;
}

section img:hover {
    cursor:crosshair;
    width: 300px;
    opacity: 1;
    filter:contrast(120%);
}

```
