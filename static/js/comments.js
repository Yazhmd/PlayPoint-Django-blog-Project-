const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
<<<<<<< HEAD
=======
const cancelButton = document.getElementById("cancelButton");

>>>>>>> parent of f44fa9c (Add: last edits)

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update Comment Edit";


        cancelButton.classList.remove("d-none");

        commentForm.setAttribute("action", `/reviews/edit_comment/${commentId}`);
    });
}

const deleteButtons = document.getElementsByClassName("btn-delete");
<<<<<<< HEAD

const deleteConfirm = document.getElementById("deleteConfirm");



=======
const deleteConfirm = document.getElementById("deleteConfirm");
const reviewSlug = document.querySelector("#review-slug").dataset.slug;
>>>>>>> parent of f44fa9c (Add: last edits)

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
<<<<<<< HEAD
 */
 

const reviewSlug = document.querySelector("#review-slug").dataset.slug;  
=======
 * 
 */

>>>>>>> parent of f44fa9c (Add: last edits)

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `/app_blog/${reviewSlug}/delete_comment/${commentId}`;
    });
<<<<<<< HEAD
}

=======
}
>>>>>>> parent of f44fa9c (Add: last edits)
