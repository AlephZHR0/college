class Book {
    String bookName;
    String author;
    String publisher;
    String genre;
    int yearPublished;
    int price;
    int numPages;
    int numChapters;
    int isnb;
    boolean isHardCover;


    public Book(String bookName, String author, int numChapters, int isnb) {
        this.bookName = bookName;
        this.author = author;
        this.numChapters = numChapters;
        this.isnb = isnb;
    }
}