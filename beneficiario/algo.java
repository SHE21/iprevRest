class Main {  
  public static void main(String args[]) {

    int[] mat = {10, 9, 12, 8, 2, 13, 7, 5, 3, 1};
    int[] newMat = new int[mat.length];

    int counter = 0;
    int number = 0;

    for(int i = 0; i < mat.length; i++){

      for(int j = 0; j < mat.length; j++){

          if(mat[i] > mat[j] && mat[i] != mat[j]){
            counter++;
            
          }

          number = mat[i];
      }
      //adiciona aqui
      newMat[counter] = number;
      counter = 0;
      
    }

    for(int n = 0; n < newMat.length; n++){
      System.out.println(newMat[n]);
    }
  } 
}