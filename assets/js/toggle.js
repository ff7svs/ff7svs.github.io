function toggleblock(blockId)
{
    var block = document.getElementById(blockId);
    if (block.style.display == 'none') {
        block.style.display = 'block' ;
    } else {
        block.style.display = 'none' ;
    }
}

function toggleclass(className)
{
    var elements = document.getElementsByClassName(className);
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = elements[i].style.display == 'none' ? 'inline' : 'none';
    }
}