
function Collapsible(fullTextElement, shortTextElement, toggleElement, options) {
    let noOfTextContentToShow = options?.noOfTextContentToShow || 350;
    var fullText = fullTextElement.textContent;

    //hide full text element
    fullTextElement.style.display = 'none'; 

    // set content in short text Element
    var shortText = fullText.substring(0, noOfTextContentToShow); 
    shortTextElement.textContent = shortText;

    if (fullText.length < noOfTextContentToShow) {
        shortTextElement.textContent = fullText;
        toggleElement.style.display = 'none';
        return
    } 

    
    toggleElement.addEventListener('click', function (event) {
        event.preventDefault();
        toggleDisplay(shortTextElement)
        toggleDisplay(fullTextElement)
        toggleElement.textContent = fullTextElement.style.display === 'none' ? 'see more' : 'see less';
    });
}

function toggleDisplay(element) {
    element.style.display = ( element.style.display === 'none' ? 'block' : 'none');
}