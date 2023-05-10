package interfaces

interface EmailValidator {
    var input:String

    fun isValidEmail():Boolean = input.contains("@")


}


class RegistrationForm(override var input:String=""):EmailValidator{

    fun checkMail(){
        if (isValidEmail()) {
            print("${input} is a valid email")
        } else{
            print("${input} is not a valid email")
        }
    }
}


fun runForm(){
    var form = RegistrationForm(input="sai@gmail.com")
    form.checkMail()
    form.input="said"
    form.checkMail()
}