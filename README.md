# README - Guía para editar el Programa Electoral "Solucions" en Sitges

Este repositorio contiene el código de la página web del programa electoral del partido **"Solucions"** en Sitges. Este documento te guiará sobre cómo puedes **editar el contenido de la página web** para actualizar información como textos, imágenes y enlaces.

## ¿Qué necesitas saber?

Este proyecto está basado en HTML, CSS y JavaScript. Si quieres actualizar el contenido de la página, no necesitas saber programar, pero sí necesitarás saber cómo editar un archivo de texto (en este caso, el archivo HTML).

El archivo principal que controla el contenido visible en la página web es **`index.html`**. En este archivo se encuentran los textos, imágenes, y enlaces que puedes personalizar.

### Archivos principales del proyecto:
1. **`index.html y /templates`**: Estos son los archivos principales donde se encuentra el contenido de la página (textos, enlaces, imágenes, etc.).
2. **`/static/style.css`**: Contiene los estilos visuales de la página, como los colores y el diseño.
3. **`/static/img/`**: Carpeta con las imágenes utilizadas en el sitio web.

## Pasos para editar la página

### 1. **Cambiar los textos de la página**

La mayor parte del contenido en la página web está en **texto** (como el título, las secciones del programa electoral, la descripción del candidato, etc.).

- **¿Dónde está el contenido?**
    - El contenido está en el archivo `index.html`. Cada bloque de texto importante está rodeado por etiquetas `<p>`, `<h1>`, `<h2>`, etc.
    - Ejemplo: Si quieres cambiar el título que aparece en la parte superior, busca este bloque:

    ```html
    <h1>SOLUCIONS</h1>
    <h2>El Partit de Tots</h2>
    <h2>Sitges</h2>
    ```

    - Puedes cambiar el texto dentro de las etiquetas `<h1>` o `<h2>`.

- **¿Cómo editarlo?**
    1. Abre el archivo `index.html` con un editor de texto. Si no tienes uno, puedes usar editores gratuitos como [Notepad++](https://notepad-plus-plus.org/) o [VS Code](https://code.visualstudio.com/).
    2. Busca el texto que deseas cambiar (como el ejemplo anterior) y simplemente reemplázalo por lo que quieras mostrar en la página.

### 2. **Actualizar enlaces en el menú de navegación**

Si deseas cambiar algún enlace en el menú (por ejemplo, el enlace a "Vilanova i la Geltrú" o "Olivella"), sigue estos pasos:

- **¿Dónde están los enlaces?**
    - Los enlaces están dentro de la etiqueta `<ul class="navbar-nav ml-auto">`. Aquí puedes cambiar tanto el nombre visible del enlace como la URL a la que apunta.

    Ejemplo de cómo se ve un enlace en el código:
    ```html
    <li class="nav-item">
        <a class="nav-link" href="templates/vilanova.html">Vilanova i la Geltrú</a>
    </li>
    ```

    - Si quieres cambiar el texto del enlace, edita lo que está dentro de las etiquetas `<a>`, por ejemplo, cambia "Vilanova i la Geltrú" a "Nueva Sección".
    - Si quieres cambiar la URL del enlace, edita el valor de `href`, por ejemplo:
      ```html
      <a class="nav-link" href="templates/nueva_seccion.html">Nueva Sección</a>
      ```

### 3. **Cambiar las imágenes del sitio**

Para cambiar una imagen (como el logo o las fotos en el carrusel), sigue estos pasos:

- **¿Dónde se encuentran las imágenes?**
    - Las imágenes están en la carpeta `/static/img/`. Por ejemplo, el logo se llama `logoSolucions.webp` y está en la carpeta `img`.

- **¿Cómo cambiar una imagen?**
    1. Primero, **prepara tu nueva imagen**. Asegúrate de que tenga el mismo nombre que la imagen que quieres reemplazar (o actualiza el código si decides usar un nombre diferente).
    2. Coloca la nueva imagen en la carpeta `static/img/`.
    3. En el archivo `index.html`, busca la etiqueta `<img>` que hace referencia a la imagen que quieres cambiar. Por ejemplo, para el logo:

    ```html
    <img src="/static/img/logoSolucions.webp" alt="Logo">
    ```

    - Si la imagen tiene un nombre diferente, cambia el valor de `src` para que apunte a la nueva imagen. Ejemplo:

    ```html
    <img src="/static/img/nuevoLogo.webp" alt="Logo">
    ```

### 4. **Actualizar las redes sociales**

Si necesitas actualizar los enlaces a redes sociales, busca el bloque que contiene los íconos de redes sociales en el archivo `index.html`:

```html
<div class="d-flex justify-content-center ">
    <a href="https://x.com/solucions_org" target="_blank" class="social-icon mx-2" title="X">
        <i class="fab fa-x"></i>
    </a>
    <a href="https://www.instagram.com/solucions_org" target="_blank" class="social-icon mx-2" title="Instagram">
        <i class="fab fa-instagram"></i>
    </a>
    <a href="https://www.facebook.com/solucionselpartitdetots" target="_blank" class="social-icon mx-2" title="Facebook">
        <i class="fab fa-facebook"></i>
    </a>
</div>
