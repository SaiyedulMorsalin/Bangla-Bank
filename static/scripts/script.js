
const addNewListItem = () => {
    let ulItem = document.getElementById('how-to-works-ul')
    ulItem.innerHTML = `
    <li class="leading-10">
        <i class="fa-regular fa-circle-dot fa-sm hover:text-blue-900" style=""></i><span class="ml-3">1. Tell Us About Your Business</span>
    </li>
    <li class="leading-10">
        <i class="fa-regular fa-circle-dot fa-sm hover:text-blue-900" style=""></i><span class="ml-3">2. Tell Us About Your Business</span>
    </li>
    <li class="leading-10">
        <i class="fa-regular fa-circle-dot fa-sm hover:text-blue-900" style=""></i><span class="ml-3">3. Tell Us About Your Business</span>
    </li>
    <li class="leading-10">
        <i class="fa-regular fa-circle-dot fa-sm hover:text-blue-900" style=""></i><span class="ml-3">4. Tell Us About Your Business</span>
    </li>
    <li class="leading-10">
        <i class="fa-solid fa-circle fa-sm hover:text-blue-900" style=""></i><span class="ml-3">5. All Done</span>
    </li>
    
    `

}