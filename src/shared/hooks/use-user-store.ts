import { create } from "zustand";
import {
  getCurrentUserAction,
  getStreakAction,
  getCompletedLearningItemsAction,
  getBookmarksAction,
  toggleBookmarkAction,
  completeLearningItemAction,
  uncompleteLearningItemAction,
} from "@/app/actions";
import { getLevelFromXp } from "@/modules/progress/xp";

interface UserState {
  user: any | null;
  streak: any | null;
  completedLearningItems: number[];
  bookmarks: number[];
  isLoading: boolean;

  fetchUserData: () => Promise<void>;
  toggleBookmark: (learningItemId: number) => Promise<void>;
  completeLearningItem: (learningItemId: number, xpReward: number) => Promise<any>;
  uncompleteLearningItem: (learningItemId: number) => Promise<any>;
}

export const useUserStore = create<UserState>((set, get) => ({
  user: null,
  streak: null,
  completedLearningItems: [],
  bookmarks: [],
  isLoading: false,

  fetchUserData: async () => {
    set({ isLoading: true });
    try {
      const [user, streak, completed, bookmarks] = await Promise.all([
        getCurrentUserAction(),
        getStreakAction(),
        getCompletedLearningItemsAction(),
        getBookmarksAction(),
      ]);
      set({ user, streak, completedLearningItems: completed, bookmarks });
    } catch (e) {
      console.error("Error fetching user data in store", e);
    } finally {
      set({ isLoading: false });
    }
  },

  toggleBookmark: async (learningItemId: number) => {
    const { bookmarks } = get();
    const isBookmarked = bookmarks.includes(learningItemId);

    const updated = isBookmarked
      ? bookmarks.filter((id) => id !== learningItemId)
      : [...bookmarks, learningItemId];
    set({ bookmarks: updated });

    try {
      const serverResult = await toggleBookmarkAction(learningItemId);
      if (serverResult !== !isBookmarked) {
        const freshBookmarks = await getBookmarksAction();
        set({ bookmarks: freshBookmarks });
      }
    } catch (e) {
      console.error("Failed to toggle bookmark", e);
      set({ bookmarks });
    }
  },

  completeLearningItem: async (learningItemId: number, xpReward: number) => {
    const { completedLearningItems, user } = get();
    if (completedLearningItems.includes(learningItemId)) {
      return { success: true, alreadyCompleted: true };
    }

    // Optimistically update on client immediately
    const updatedCompleted = [...completedLearningItems, learningItemId];
    const updatedUser = user
      ? {
          ...user,
          xp: user.xp + xpReward,
          level: getLevelFromXp(user.xp + xpReward),
        }
      : null;
    
    set({ completedLearningItems: updatedCompleted, user: updatedUser });

    try {
      const result = await completeLearningItemAction(learningItemId, xpReward);
      
      // Parallelize state refreshes in background to align details (level ups, streaks, achievements)
      const [freshUser, freshStreak, freshCompleted] = await Promise.all([
        getCurrentUserAction(),
        getStreakAction(),
        getCompletedLearningItemsAction(),
      ]);

      set({ user: freshUser, streak: freshStreak, completedLearningItems: freshCompleted });
      return result;
    } catch (e) {
      console.error("Failed to complete learning item", e);
      // Revert state on failure
      set({ completedLearningItems, user });
      throw e;
    }
  },

  uncompleteLearningItem: async (learningItemId: number) => {
    const { completedLearningItems, user } = get();
    if (!completedLearningItems.includes(learningItemId)) {
      return { success: true, alreadyUncompleted: true };
    }

    // Optimistically update on client immediately
    const updatedCompleted = completedLearningItems.filter((id) => id !== learningItemId);
    const updatedUser = user
      ? {
          ...user,
          xp: Math.max(0, user.xp - 100),
          level: getLevelFromXp(Math.max(0, user.xp - 100)),
        }
      : null;

    set({ completedLearningItems: updatedCompleted, user: updatedUser });

    try {
      const result = await uncompleteLearningItemAction(learningItemId);

      // Parallelize state refreshes in background
      const [freshUser, freshStreak, freshCompleted] = await Promise.all([
        getCurrentUserAction(),
        getStreakAction(),
        getCompletedLearningItemsAction(),
      ]);

      set({ user: freshUser, streak: freshStreak, completedLearningItems: freshCompleted });
      return result;
    } catch (e) {
      console.error("Failed to uncomplete learning item", e);
      // Revert state on failure
      set({ completedLearningItems, user });
      throw e;
    }
  },
}));
