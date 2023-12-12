public class InvalidNameException extends Exception {
    String msg;

    public InvalidNameException(String msg) {
        this.msg = msg;
    }

    public InvalidNameException() {
        this.msg = "Invalid Name exception.";
    }

    @Override
    public String getMessage() {
        return "String must be in Pascal Case." + this.msg;
    }
}
