export default function getStudentIdsSum(studentArray){
    return studentArray.reduce((total,student)=> student.id + total, 0);
}
