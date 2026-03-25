1. Don't let the agent not verify DOB. Whatever DOB user is giving agent should be fine with it and should not ask the user to correct it. 
2. Thank you card
3. Form Card type. 
    - Form fields: Name, Last 4 digits of SSN, DOB and Claim ID
    - They are supposed to populated in the UI as user speak these fields
    - Intially user may tell some of these fields. So, partially only those fields supposed to be populated in the form card.
    - So, I think we have to trigger the form card type multiple times for this.
    
---

1. Don't use `claim_id` for verification
    - Remove claim_id from identity form
    - Don't ask for claim_id from caller
2. Add step for OTP verification
