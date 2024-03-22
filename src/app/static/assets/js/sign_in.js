import { callAPI, showToast } from "./misc.js";
document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById('login_form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        callAPI('POST', '/login', formData).then(()=>{
            showToast("Login success", 'success')
            window.location.href = 'dashboard'
        }).catch((e)=>{
            showToast(e, 'danger')
        })
        
    });
});