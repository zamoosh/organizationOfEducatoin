export function getElement(selection){
    const element = document.querySelectorAll(selection);
    if (element.length ===0)
        return new Error(`no element with this ${selection}`)
    if(element.length ===1)
        return element[0]
    return element;
}