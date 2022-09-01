export const FormComponent = ({Form, handleSubmit, Input, password, password2, SubmitButton, SubmitButtonIcon, submitButtonText, signInUrl}) => (
    <Form onSubmit={handleSubmit}>
        <Input 
            type="text" 
            id="username"
            placeholder="Username"
            required
        />
        <Input 
            type="password" 
            id="password"
            placeholder="Password"
            required
        />
        <Input 
            type="password" 
            id="password2"
            placeholder="Confirm Password"
            required
        />
        <p tw="mt-8 text-sm text-gray-600 text-center">
            {password2 !== password ? "Passwords do not match" : ""}
        </p>
        <SubmitButton type="submit">
        <SubmitButtonIcon className="icon" />
        <span className="text">{submitButtonText}</span>
        </SubmitButton>

        <p tw="mt-8 text-sm text-gray-600 text-center">
        Already have an account?{" "}
        <a href={signInUrl} tw="border-b border-gray-500 border-dotted">
            Sign In
        </a>
        </p>
    </Form>
);