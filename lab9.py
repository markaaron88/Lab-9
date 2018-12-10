def getSound():
  return makeSound( pickAFile() )

def clip(source, start, end):
  target = makeEmptySound(end - start,11500)
  targetIndex = 0
  for sourceIndex in range(start, end):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue * 20)
    targetIndex = targetIndex + 1
  return target

  
def copy(source, target, start):
  targetIndex = start
  for sourceIndex in range(0, getLength(source)):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue *20)
    targetIndex = targetIndex + 1      
  return target
        
         
# this function receives a sound and returns the clip in reverse
def reverse(sound):
  target = makeEmptySound(getLength(sound), 11500)
  x = getLength(sound) - 1
  for sourceIndex in range(0, getLength(target)):
    sourceValue = getSampleValueAt(sound, sourceIndex)
    setSampleValueAt(target, x, sourceValue * 5)
    x -= 1
  return target        

def collage(sound1,sound2,sound3,sound4,sound5):
  target = makeEmptySoundBySeconds(15, 11500 )
  #target = makeEmptySound((end - start, 11500))
  copySound=copy(sound1, target, 0)
  copySound=copy(sound2, target, getLength(sound1) + int(0.1 * getSamplingRate(sound1))*30)
  sound3Length = getLength(sound1) + getLength(sound2)
  copySound=copy(sound3, target, sound3Length + int(0.1 * getSamplingRate(sound2)) * 30 )
  sound4Length = sound3Length + getLength(sound3)
  copySound=copy(sound4, target, sound4Length + int(0.1 * getSamplingRate(sound3)) * 30)
  sound5Length = sound4Length + getLength(sound4)
  copySound=copy(sound5, target, sound5Length + int(0.1 * getSamplingRate(sound4)) * 30 )
  return target
