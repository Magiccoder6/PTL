import { callAPI, showToast } from "./misc.js";
document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('register_form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        callAPI('POST', '/register', formData).then(()=>{
            showToast('Registered successfully', 'success')
            window.location.href = '/'
        }).catch((e)=>{
            showToast(e, 'danger')
        })
        
    });
});